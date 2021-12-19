function ValidFunc(){
    const inputObj = document.getElementById("age")
    if(!inputObj.checkValidity()){
        document.getElementById("demo").innerHTML = inputObj.validationMessage;
    }
    else{
        document.getElementById("demo").innerHTML = "Thank you for submitting";
    }
}