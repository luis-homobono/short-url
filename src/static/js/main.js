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
}