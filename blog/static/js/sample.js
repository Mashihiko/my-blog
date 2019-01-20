
var thisOffset;
$(window).on('load',function(){
	thisOffset = $('.fixed').offset().top + $('.fixed').outerHeight();
});
 
$(window).scroll(function(){
	if( $(window).scrollTop() > thisOffset){
		// 特定の要素を超えた
        $('.fixed').fadeOut(100);
	} else {
	// 特定の要素を超えていない
         $('.fixed').fadeIn(100);
	}
});

$(function () {
    $('.glyphicon-trash').click(function () {
        $("#hide_block").css("visibility", "visible");
    });
});

$(function () {
    $('#no_botton').click(function () {
        $("#hide_block").css("visibility", "hidden");
    });
});


// 確認用　$("#text").css("color","red"):
