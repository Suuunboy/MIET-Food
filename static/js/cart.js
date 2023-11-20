var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function() {
        var productid = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productid, 'action:', action)
        console.log('USER:', user)
    })
}