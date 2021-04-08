$(function (){
    // custom file input
    bsCustomFileInput.init()
    // show current year on footer
    $('current-year').text(new Date().getFullYear());

    // toggle left menu
    $('#show-more-option').on('click', function (){
        $('.options-menu').toggleClass('open');
        $('.content-block').toggleClass('open');
    });


    // category book show/hide
    $('.category-buttons button, #collapse-category > a.category').on('click', function (){
        $('.books .all-book').hide();
        $('.books .all-book.book-category-' + $(this).data('id')).show();
    });

    // status book show/hide
    $('#status-navbar > p.status-pra').on('click', function (){
        $('.books .all-book').hide();
        $('.books .all-book.book-status-' + $(this).data('status')).show();
        console.log('.books .all-book.book-status-' + $(this).data('status'))
    });



})