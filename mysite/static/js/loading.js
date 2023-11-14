// function test(imageName) {
//     LoadingWithMask ("your site\'s image path");
//     setTimeout("closeLoadingWithMask()", 3000);

// }

// function LoadingWithMask(gif) {
//     let maskHeight = $(document).height();
//     let maskWidth = window.document.body.clientWidth;

//     let mask = "<div id='mask' style='position:absolute; z-index:9000; background-color:#000000; display:none; left:0; top:0;'></div>";
//     let loadingImg = 'Spinner';
//     loadingImg += " <img src='"+ gif + "' style='position: absolute; display: block; margin: 0px auto;'/>";

//     $('body')
//         .append(mask)

//     $('#mask').css({
//         'width' : maskWidth,
//         'height' : maskHeight,
//         'opacity' : '0.3'
//     });

//     $('#mask').show();

//     $('#loadingImg').append(loadingImg);
//     $('#loadingImg').show();
    
//     }
// function closeLoadingWithMask(){
//     $('#mask, #loadingImg').hide();
//     $('#mask, #loadingImg').empty();
// }

function showLoading() {
    let maskHeight = $(document).height();
    let maskWidth = window.document.body.clientWidth;

    let mask = "<div id='mask' style='position:absolute; z-index:9000; background-color:#000000; display:block; left:0; top:0;'></div>";
    let loadingImg = '<div id="loadingImg" style="position: absolute; display: block; margin: 0px auto; z-index:10000;">';
    loadingImg += "<img src='{% static 'images/loading.gif' %}' style='position: absolute; display: block; margin: 0px auto;'/></div>";

    $('body').append(mask);

    $('#mask').css({
        'width' : maskWidth,
        'height' : maskHeight,
        'opacity' : '0.5'
    });

    $('#mask').show();

    $('#loadingImg').html(loadingImg);
    $('#loadingImg').show();    
}

function hideLoading() {
    $('#mask, #loadingImg').hide();
    $('#mask, #loadingImg').empty();
}
