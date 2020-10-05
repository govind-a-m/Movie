var WarningState = "NONE"
var form;


function AddPost()
{
    var body = document.getElementById("body")
    cloneForm = body.insertBefore(document.getElementById("HiddenPostForm").cloneNode(true),body.firstElementChild.nextSibling);
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

function highlight(del)
{   var m_card = del.attributes['belongsto'].value; 
    document.getElementById(m_card).style.borderColor = "#d63227";
    document.getElementById(m_card).className = "card border-2 mb-3 body_bgd";
    a = document.getElementById(m_card);
    document.getElementById('modal_text').innerHTML = 'delete movie '+document.getElementById(m_card).attributes['movie_name'].value;
    document.querySelector("#modal_text").setAttribute("movie_id",document.getElementById(m_card).attributes['movie_id'].value);
}

function dehighlight(del)
{
    document.getElementById(del.attributes['belongsto'].value).style.borderColor = "#000066";
    document.getElementById(del.attributes['belongsto'].value).className = "card border-0 mb-3 body_bgd";
}

function SendDeleteForm()
{   
    document.querySelector("#Delete_MovieId").value = document.querySelector("#modal_text").getAttribute("movie_id");
    document.querySelector("#DeleteMovieForm").submit();
}

function LikeUnlike(likebtn){
    var likeInp = document.getElementById("LikeInput");
    var MovLikeInp = document.getElementById("MovieLikeInput");
    let movie_id = likebtn.attributes['movie_id'].value;
    if(likebtn.className=="btn btn-outline-danger btn-sm float-left")
    {
        likebtn.className = "btn btn-danger btn-sm float-left";
        likeInp.value = "like";
        MovLikeInp.value = likebtn.attributes['movie_name'].value
        $.ajax({
                url: '/Likes',
                data: $('#LikeForm').serialize(),
                type: 'POST',
                success: function(response){
                OnLikeResponse(response,movie_id);
                },
                error: function(error){
                    console.log(error);
                }
        });
    }
    else
    {
        likebtn.className = "btn btn-outline-danger btn-sm float-left";
        likeInp.value = "unlike";
        MovLikeInp.value = likebtn.attributes['movie_name'].value;
        $.ajax({
                url: '/Likes',
                data: $('#LikeForm').serialize(),
                type: 'POST',
                success: function(response){
                OnLikeResponse(response,movie_id);
                },
                error: function(error){
                    console.log(error);
                }
        });
    }
}

function OnLikeResponse(response,movie_id){
    rsp = JSON.parse(response);
    liketext_id = "LikedCountText_"+movie_id;
    if(rsp.OP_STAT=="ADDED_TO_LIKED")
    {
       document.getElementById(liketext_id).innerHTML = rsp.LikeCount.toString()+" "+"likes";
    }
    else if(rsp.OP_STAT=='REMOVED_FROM_LIKED')
    {
        document.getElementById(liketext_id).innerHTML = rsp.LikeCount.toString()+" "+"likes";
    }
    else
    {
        console.log("invalid operation")
    }
}

function QueryLikeStatus(likeimg){
    console.log(likeimg);
    var likebtnid = likeimg.attributes['likebtnid'].value;
    $.ajax({
                url: '/LikeQuery',
                data: {"movie_name":likeimg.attributes['movie_name'].value},
                type: 'POST',
                success: function(response){
                onQueryLikeStatus(response,likebtnid);

                },
                error: function(error){
                    console.log(error);
                }
        });
}

function onQueryLikeStatus(response,likebtnid){
    let rsp = JSON.parse(response);
    let likecounttext_id = likebtnid.replace("likebtn_","LikedCountText_");
    if(rsp.Liked=='YES')
    {
        document.getElementById(likebtnid).className = "btn btn-danger btn-sm float-left";
        document.getElementById(likecounttext_id).innerHTML = rsp.LikeCount.toString()+" "+"likes";
    }
    else if(rsp.Liked=='NO')
    {
        document.getElementById(likebtnid).className = "btn btn-outline-danger btn-sm float-left";
        document.getElementById(likecounttext_id).innerHTML = rsp.LikeCount.toString()+" "+"likes";
    }
}

function QueryUsername(){
        $.ajax({
                url: '/UsernameQuery',
                data: {},
                type: 'GET',
                success: function(response){
                onQueryUsername(response);
                },
                error: function(error){
                    console.log(error);
                }
        });
}


function onQueryUsername(response){
    rsp = JSON.parse(response);
    if(rsp.UserName!='UNKNOWN')
    {
        document.getElementById('H_UserName').value = rsp.UserName;
    }
}

