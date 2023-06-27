var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, "Action:", action)

        console.log("USER:", user)
        if (user == "AnonymousUser"){
            console.log("Not logged in")
        } else {
            updateUserOrder(productId, action)
        }
    })  // listen for a click, what do when click
}



function updateUserOrder(productId, action){
    console.log('User is logged in, sending data')

    var url = '/update_item/' // url we send data to

    fetch(url, {
        method: 'POST',
        headers: {'Content-Type':'application/json'}, //lookup and research fetch apis after
        body:JSON.stringify({'productId': productId, 'action': action})
    })
    
    .then((response) =>{
        return response.json()
    })

    .then((data) => {
        console.log('data:', data)
    })
}