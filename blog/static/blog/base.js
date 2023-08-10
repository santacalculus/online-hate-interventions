"use strict"



function openCommentBox() {
    
    if (document.getElementById('CommentForm').checkValidity()) {
        var commboxdiv = document.getElementById("id_addbtn")
        $('#exampleModal').modal('hide'); // Close the modal
        commboxdiv.innerHTML = ""
        
        var x = document.getElementById("id_postbox")
        x.style.display = "block"        
        // var postboxdiv = document.createElement("div")
        // postboxdiv.id = "id_postboxdiv"
        // commboxdiv.appendChild(postboxdiv)
        // //creating form element
        // var postform = document.createElement("form")
        // postform.action = "{% url 'page' %}"
        // postform.method = "POST"
        // postform.className = "post-input-box"
        // postboxdiv.appendChild(postform)
        // //label
        // var postlabel = document.createElement("label")
        // postlabel.id = "id_post_input_label"
        // postlabel.innerHTML = "Add Comment: "
        // postform.appendChild(postlabel)
        // //input tag
        // var postinput = document.createElement("input")
        // postinput.type = "text"
        // postinput.id = "id_post_input_text"
        // postinput.name = "text"
        // postform.appendChild(postinput)
        
        // //csrf
        // var csrfToken = getCookie('csrftoken');
        // var csrfInputElement = document.createElement("input");
        // csrfInputElement.type = "hidden";
        // csrfInputElement.name = "csrfmiddlewaretoken";
        // csrfInputElement.value = csrfToken;
        // postform.appendChild(csrfInputElement);
        // //submit button
        // var postbutton = document.createElement("button")
        // postbutton.type = "submit"
        // postbutton.id = "id_postbutton"
        // postbutton.className = "btn btn-primary"
        // postbutton.innerHTML = "Submit"
        // postform.appendChild(postbutton)



    } else {
        var invalid = document.getElementById("id_invalid_fields")
        invalid.innerHTML = "Please answer all the questions."
        invalid.classList.add("alert", "alert-danger");
    }
    
    
};

// Function to get cookie by name
function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length === 2) return parts.pop().split(";").shift();
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
