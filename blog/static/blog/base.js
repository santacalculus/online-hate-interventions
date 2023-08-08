"use strict"

function openCommentBox() {
    if (document.getElementById('CommentForm').checkValidity()) {
        var commboxdiv = document.getElementById("id_comment_space")
        $('#exampleModal').modal('hide'); // Close the modal
        commboxdiv.innerHTML = ""
        


    } else {
        var invalid = document.getElementById("id_invalid_fields")
        invalid.innerHTML = "Please answer all the questions."
        invalid.classList.add("alert", "alert-danger");
    }
    
}

// function loadComments() {
//     let xhr = new XMLHttpRequest()
//     xhr.onreadystatechange = function() {
//         if (this.readyState != 4) return
//         if (xhr.status == 200) {
//             let response = JSON.parse(xhr.responseText)
//             let commentresponse = response.comments
//             updateComments(commentresponse)
//             return
//         }

//         if (xhr.status == 0) {
//             displayError("Cannot connect to server")
//             return
//         }
    
    
//         if (!xhr.getResponseHeader('content-type') == 'application/json') {
//             displayError("Received status=" + xhr.status)
//             return
//         }
    
//         let response = JSON.parse(xhr.responseText)
//         if (response.hasOwnProperty('error')) {
//             displayError(response.error)
//             return
//         }
    
//         displayError(response)
//     }
        
// }
