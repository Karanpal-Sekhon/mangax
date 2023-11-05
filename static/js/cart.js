$(".add-cart").on("click", function() {

    // let productCard = $(this).closest(".product-card");
    let product_pid = $(this).data("pid");
    let product_title = $(this).data("title");
    let product_price = $(this).data("price");
    let product_image = $(this).data("image");

    
    let this_val = $(this);

    console.log("Product Title:", product_title);
    console.log("Product pid:", product_pid);
    console.log("Product Price:", product_price);
    console.log("Current Element:", this_val);
    console.log("Product Image:", product_image)

    $.ajax({
        url : '/add-to-cart',
        data: {
            'pid' : product_pid,
            'title': product_title,
            'price': product_price,
            'image': product_image
        },

        dataType: 'json',
        beforeSend: function(){
            console.log("Adding product to cart")
        },
        success: function(res){
            this_val.html("✔ Item added to cart!")
            console.log("Added product to cart")
            // $(".cart-items.count").text(response.totalcartitems)

            setTimeout(function() {
                this_val.html("Add to Cart");
            }, 1000); // Adjust the delay duration as needed
        }
    })
});