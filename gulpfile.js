const gulp = require('gulp');
const minifycss = require('gulp-clean-css');
const uglify = require('gulp-uglify');
const concat = require('gulp-concat');
const rename = require('gulp-rename');
const runSequence = require('run-sequence');

gulp.task('minify-css', function() {
  return gulp.src('./src/css/*')
    .pipe(minifycss({
      compatibility: 'ie8'
    }))
    .pipe(rename('aladin.min.css'))
    .pipe(gulp.dest('./dist/'));
});

gulp.task('minify-js', function() {
  return gulp.src('./dist/aladin.js')
    .pipe(uglify({
      preserveComments: 'license'
    }))
    .pipe(rename('aladin.min.js'))
    .pipe(gulp.dest('./dist/'));
});

gulp.task('concat-js', function() {

  const filenames = ['cds.js', 'json2.js', 'Logger.js', 'jquery.mousewheel.js',
    'RequestAnimationFrame.js', 'Stats.js', 'healpix.min.js', 'astroMath.js',
    'projection.js', 'coo.js', 'fits.js', 'CooConversion.js', 'Sesame.js',
    'HealpixCache.js', 'Utils.js', 'URLBuilder.js', 'MeasurementTable.js',
    'Color.js', 'AladinUtils.js', 'ProjectionEnum.js', 'CooFrameEnum.js',
    'Downloader.js', 'CooGrid.js', 'Footprint.js', 'Popup.js', 'Circle.js',
    'Polyline.js', 'Overlay.js', 'Source.js', 'ProgressiveCat.js', 'Catalog.js',
    'Tile.js', 'TileBuffer.js', 'ColorMap.js', 'HpxKey.js', 'HpxImageSurvey.js',
    'HealpixGrid.js', 'Location.js', 'View.js', 'Aladin.js'
  ];
  const files = filenames.map(name => './src/js/' + name);

  return gulp.src(files)
    .pipe(concat('aladin.js'))
    .pipe(gulp.dest('./dist/'));
});

// i have a deploy script that copies it to a testing environment
gulp.task('deploy', function() {
  require('child_process').exec('./deploy.sh')
  return 0;
});

gulp.task('build', function(cb) {
  runSequence(['concat-js', 'minify-css'], 'minify-js', cb);
});

gulp.task('default', function(cb) {
  return runSequence('build', 'deploy', cb);
});
