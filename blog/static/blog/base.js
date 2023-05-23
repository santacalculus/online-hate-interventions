function openCommentBox() {
    if (document.getElementById('CommentForm').checkValidity()) {
        commboxdiv = document.getElementById("id_comment_space")
        $('#exampleModal').modal('hide'); // Close the modal
        commboxdiv.innerHTML = ""
        console.log("ok")
    } else {
        invalid = document.getElementById("id_invalid_fields")
        invalid.innerHTML = "Please answer all the questions."
        invalid.classList.add("alert", "alert-danger");
    }
    
}