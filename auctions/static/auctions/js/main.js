document.addEventListener("DOMContentLoaded", function () {

    const link = docuemnt.querySelectorAll('.item')
    const id = eval(document.querySelector('#id').innerHTML)
    console.log(id)
    link.forEach(i => {
        console.log(i)
        i.onlcick() = () => {
            getItem(id)
        }
    })


    function getItem(id) {
        fetch(`listing/${id}`)
            .then(response => response.json())
            .then(data => {

                if (data.creator == 'yes') {

                    document.querySelector('#bid-form').style.display = 'none'
                    document.querySelector('#close').style.display = 'block'
                }
                else {
                    if (data.won == yes) {
                        document.querySelector('.win').style.display = 'block'
                        document.querySelector('#bid-form').style.display = 'none'
                    }

                }
            })
    }

})