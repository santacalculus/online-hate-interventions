function openCommentBox() {
    if (document.getElementById('CommentForm').checkValidity()) {
        commboxdiv = document.getElementById("id_comment_space")
        $('#exampleModal').modal('hide'); // Close the modal
        commboxdiv.innerHTML = ""
        var card = document.createElement('div')
        card.className = 'card col-6'
        // Create card body
        var cardBody = document.createElement('textarea')
        cardBody.className = 'card-body'
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
        invalid = document.getElementById("id_invalid_fields")
        invalid.innerHTML = "Please answer all the questions."
        invalid.classList.add("alert", "alert-danger");
    }
    
}