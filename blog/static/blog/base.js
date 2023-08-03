"use strict"

function openCommentBox() {
    if (document.getElementById('CommentForm').checkValidity()) {
        var commboxdiv = document.getElementById("id_comment_space")
        $('#exampleModal').modal('hide'); // Close the modal
        commboxdiv.innerHTML = ""
        var card = document.createElement('div')
        card.className = 'card col-6'
        
        
        var cardHeader = document.createElement('div')
        cardHeader.className = 'card-header'
        // cardHeader.style.fontWeight = 'bold';
        cardHeader.textContent = "Add Comment"

        // Create card footer
        var cardFooter = document.createElement('div')
        cardFooter.className = 'card-footer'
        
        var cardSubmit = document.createElement('button')
        cardSubmit.className = 'btn btn-primary'
        cardSubmit.textContent = "Comment"

        cardFooter.appendChild(cardSubmit)
        
        // Create card body
        var cardBody = document.createElement('textarea')
        cardBody.className = 'card-body'
        cardBody.id = 'id_comment_input'
        cardBody.placeholder = 'Join the discussion!'
        cardBody.rows = 3
        cardBody.style.overflowX = "auto"
        cardBody.style.border = "none"
        

        // Append elements
        card.appendChild(cardHeader);
        card.appendChild(cardBody);
        card.appendChild(cardFooter);

        // Append card to container
        var cardContainer = document.getElementById('cardContainer');
        cardContainer.appendChild(card);


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
