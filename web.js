
function nilaiakhir(){
	var ntgs = parseInt(document.form.ntgs.value);
	var nuts = parseInt(document.form.nuts.value);
	var nuas = parseInt(document.form.nuas.value);
	var nhuruf = "";
	var nakhir = (parseInt(ntgs)*20/100) + (parseInt(nuts)*35/100) + (parseInt(nuas)*45/100);
	document.form.nakhir.value = nakhir;

	if( nakhir > 80){
		nhuruf = "A";
	}
	else if( nakhir > 70 ){
		nhuruf = "B";
	}
	else if( nakhir > 60 ){
		nhuruf = "C";
	}
	else if( nakhir > 40 ){
		nhuruf = "D";
	} else {
		nhuruf = "E";		
	}

	document.form.nhuruf.value = nhuruf;
}

var heightInput = document.querySelector(".height-input-field");
var weightInput = document.querySelector(".weight-input-field");
var calculateButton = document.querySelector(".calculate");
var result = document.querySelector(".result");
var statement = document.querySelector(".result-statement");
var BMI, height, weight;

calculateButton.addEventListener("click", ()=>{

    height = heightInput.value;
    weight = weightInput.value;
    BMI = weight/(height**2); 
    result.innerText = BMI;

    if(BMI < 15){
        statement.innerText = "Berat badan kurang";    
    }else if((BMI > 15) && (BMI < 23.99 )){
        statement.innerText = "Normal";
    }else if((BMI > 24) && (BMI < 29)){
        statement.innerText = "Obesitas";
    }else{
        statement.innerText = "DIET BANH";
    }
}
);

