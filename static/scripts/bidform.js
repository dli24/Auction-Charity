$(".end_date").change(function(){
    let startDate = document.querySelector(".start_date").value;
    let endDate = document.querySelector(".end_date").value;

    if ((Date.parse(startDate) >= Date.parse(endDate))) {
        alert("End date should be greater than Start date");
        document.querySelector(".end_date").value = "";
    }
})
