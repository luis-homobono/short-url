function copyURL() {
    const newURL = document.getElementById("newURL");
    if (!navigator.clipboard) {
        newURL.select();
        newURL.setSelectionRange(0, 50);
        document.execCommand("copy")
    } else {
        navigator.clipboard.writeText(newURL.value).then(() => {
            alert("Copied!"); // success 
        })
            .catch(() => {
                alert("Error"); // error
            });
    }

    const btnCopy = document.getElementById("btnCopy")
    btnCopy.innerHTML = "URL Copied"
    btnCopy.classList.replace("btn-outline-success", "btn-success")

    setTimeout(() => {
        location.replace(" {{ url_for('inicio') }} ")
    }, 3000)
}

function redirect(){
    const contador = document.getElementById("contador");
    let valor = 5;
    setInterval(()=>{
        if (valor > 0){
            contador.innerHTML = valor -= 1;
        }
    }, 1000)
}
// (redirect())()