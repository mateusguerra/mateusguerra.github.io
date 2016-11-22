var gulp = require('gulp');
var rename = require('gulp-rename');
var cleanCSS = require('gulp-clean-css');

gulp.task('default', function() {
	return gulp.src('web/source/*.css')
	    .pipe(cleanCSS({compatibility: 'ie8'}))
	    .pipe(rename({ extname: '.min.css' }))
	    .pipe(gulp.dest('web/assets'));
});