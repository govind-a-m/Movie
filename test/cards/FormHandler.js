
function AddPost()
{
    var body = document.getElementById("body")
    body.insertBefore(document.getElementById("movie").cloneNode(true), parent.firstChild);
}

function upload()
{
    var reader = new FileReader();
    file = $("#UpImage")[0].files[0];
    reader.onload = function(oFREvent){
        document.getElementById("NewPoster").src = oFREvent.target.result;
    };
    reader.readAsDataURL(file);
}