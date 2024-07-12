function openForm(formName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("form-container");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].classList.remove("active");
    }
    tablinks = document.getElementsByClassName("tab-link");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].classList.remove("active");
    }
    document.getElementById(formName).classList.add("active");
    document.querySelector(`[onclick="openForm('${formName}')"]`).classList.add("active");
}

