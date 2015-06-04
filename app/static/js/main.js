/**
 * Created by hassaanali on 4/2/15.
 */


$(document.body).on('click', '.like', function () {
    var id = $(this).attr("id");
    $(this).text("Unlike");

    var likes = $(this).parent().children(".likes");

    $.get("/like/" + id, function () {
        likes.text(parseInt(likes.text()) + 1);
    });

    $(this).removeClass("like");
    $(this).addClass("unlike");

}).on('click', '.unlike', function () {
    var id = $(this).attr("id");
    $(this).text("Like");

    var likes = $(this).parent().children(".likes");

    $.get("/unlike/" + id, function () {
        likes.text(parseInt(likes.text()) - 1);
    });

    $(this).removeClass("unlike");
    $(this).addClass("like");
});


$(document.body).on('click', '.follow', function () {
    var id = $(this).attr("id");
    $(this).text("Unfollow!");

    $.get("/follow/" + id, function () {

    });

    $(this).removeClass("follow btn-success");
    $(this).addClass("unfollow btn-danger");

}).on('click', '.unfollow', function () {
    var id = $(this).attr("id");
    $(this).text("Follow!");

    var likes = $(this).parent().children(".likes");

    $.get("/unfollow/" + id, function () {

    });

    $(this).removeClass("unfollow btn-danger");
    $(this).addClass("follow btn-success");
});

$(".mark-read").click(function(){
    var id = $(this).attr("id");
    $.get("../notifications/read/" + id, function () {

    });

});