
function AddPost()
{
    var body = document.getElementById("body")
    body.insertBefore(document.getElementById("movie").cloneNode(true), parent.firstChild);
}