$(function () {
    $(".slider-for").slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        speed: 500,
        arrows: false,
        fade: true,
        asNavFor: ".sync-slider"  
    });
    $(".slider-nav").slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        speed: 500,
        asNavFor: ".sync-slider",
        centerMode: true,
        focusOnSelect: true,
        prevArrow: `<img class='slider-arrow-prev slider-arrow' weight='40px' src='${sourcePath + 'img/arrowL.png'}'>`,
        nextArrow: `<img class='slider-arrow-next slider-arrow' weight='40px' src='${sourcePath + 'img/arrowR.png'}'>`,
    });
    $(".slider-fade").slick({
        infinite: true,
        speed: 500,
        asNavFor: ".sync-slider",
        fade: true,
        cssEase: "linear"
    });
});

$('.modal').on('shown.bs.modal', function () {
    // Инициализация слайдера после появления модального окна
    $('.slider-fade').slick('setPosition');
    $('.slider-fade').addClass('open');
});