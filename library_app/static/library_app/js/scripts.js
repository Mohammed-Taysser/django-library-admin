$(function (){
    // custom file input
    bsCustomFileInput.init()
    // show current year on footer
    $('current-year').text(new Date().getFullYear());

    // toggle left menu
    $('#show-more-option').on('click', function (){
        console.log(230);
        $('.options-menu').toggleClass('open');
        $('.content-block').toggleClass('open');
    })


})