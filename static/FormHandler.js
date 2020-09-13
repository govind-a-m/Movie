var WarningState = "NONE"
var form;
function AddPost()
{
    var body = document.getElementById("body")
    cloneForm = body.insertBefore(document.getElementById("HiddenPostForm").cloneNode(true),document.getElementById("Movie_1"));
    cloneForm.id = "NewPostForm";
    cloneForm.style.display = "block";
    cloneForm.querySelector("#H_MovieName").id = "MovieName";
    cloneForm.querySelector("#H_UserName").id = "UserName";
    cloneForm.querySelector("#H_poster").id = "poster";
    cloneForm.querySelector("#H_review").id = "review";
    cloneForm.querySelector("#H_torrent_link").id = "torrent_link";
    cloneForm.querySelector("#H_dd_link").id = "dd_link";
    cloneForm.querySelector("#H_trailer_link").id = "trailer_link";
    cloneForm.querySelector("#H_submit").id = "Newsubmit";
    cloneForm.querySelector("#H_alert").id = "alert";
    form = document.getElementById("NewPostForm");
}

function upload()
{
    var reader = new FileReader();
    file = $("#UpImage")[0].files[0];
    reader.onload = function(oFREvent){
        document.getElementById("poster").src = oFREvent.target.result;
    };
    reader.readAsDataURL(file);
}

function SubmitPost()
{   alert = document.getElementById("alert");
    if(document.getElementById("MovieName").value.length == 0)
    {   
        alert.innerHTML = "Movie name cannot be left blank";
        alert.style.visibility = "visible";
        return false;
    }
    else if(document.getElementById("UserName").value.length == 0)
    {
        alert.innerHTML = "user name cannot be left blank";
        alert.style.visibility = "visible";
        return false;
    }
    else
    {   
        alert.className = "col-md-11 my-0  alert alert-warning float-left border-bottom-0 py-0";
        if(document.getElementById("poster").src.includes("blank_poster"))
        {
            if(WarningState=="blank_poster")
            {
                return true;
            }
            else
            {
                alert.innerHTML = "click on poster to add new poster";
                alert.style.visibility = "visible";
                WarningState = "blank_poster";
                return false;
            }
        }
        else if(document.getElementById("review").value.length==0)
        {
            if(WarningState=="review")
            {
                return true;
            }
            else
            {
                alert.innerHTML = "please consider adding a review";
                alert.style.visibility = "visible";
                WarningState = "review";
                return true;
            }
        }
        else if(document.getElementById("trailer_link").value.length == 0)
        {
            if(WarningState=="trailer_link")
            {
                return true;
            }
            else
            {
                alert.innerHTML = "please consider adding a trailer";
                alert.style.visibility = "visible";
                WarningState = "trailer_link";
                return false;
            }
        }
        else
        {
            return true;
        }
    }
}

