// Get the pizza size price and add it to the running Total
// then pass that running total to the next function so 
// the next function will add a particular total to the running total and so on...
//
// Keep doing this until you get all items added to the running total.
//
// Just remember that the syntax will be text1 = text1 + something + "<br>";
// So you take the orginal value and concetenate to something new and end it with
// an HTML line break so our code will write the next thing one line below instead
// of overwriting the previous print out.
function getReceipt() {
	// This initializes our string so it can get passed from  
	// function to function, growing line by line into a full receipt
	var text1 = "<h3>You Ordered:</h3>";
	var runningTotal = 0;
	var sizeTotal = 0;
	var sizeArray = document.getElementsByClassName("size");
	for (var i = 0; i < sizeArray.length; i++) {
		if (sizeArray[i].checked) {
			var selectedSize = sizeArray[i].value;
			text1 = text1+selectedSize+"<br>";
		}
	}
	if (selectedSize === "Personal Pizza") {
		sizeTotal = 6;
	} else if (selectedSize === "Medium Pizza") {
		sizeTotal = 10;
	} else if (selectedSize === "Large Pizza") {
		sizeTotal = 14;
	} else if (selectedSize === "Extra Large Pizza") {
		sizeTotal = 16;
	}
	runningTotal = sizeTotal;
	console.log(selectedSize+" = $"+sizeTotal+".00");
	console.log("size text1: "+text1);
	console.log("subtotal: $"+runningTotal+".00");
	getMeat(runningTotal,text1); // All three of these variables will be passed on to each function
};	

// With both the meat and veggie functions each item in the array will be
// 1 dollar but the first is going to be free so we can count the total
// of items in their array and subtract 1 to get the total item cost
//
// Now we can add the item cost to our running total to get the new
// running total and then pass this new running total to the next function
// Just keep up this process until we've added all items to the running total
function getMeat(runningTotal,text1) {
	var meatTotal = 0;
	var selectedMeat = [];
	var meatArray = document.getElementsByClassName("meats");
	for (var j = 0; j < meatArray.length; j++) {
		if (meatArray[j].checked) {
			selectedMeat.push(meatArray[j].value);
			console.log("selected meat item: ("+meatArray[j].value+")");
			text1 = text1+meatArray[j].value+"<br>";
		}
	}
	var meatCount = selectedMeat.length;
	if (meatCount > 1) {
		meatTotal = (meatCount - 1);
	} else {
		meatTotal = 0;
	}
	runningTotal = (runningTotal + meatTotal);
	console.log("total selected meat items: "+meatCount);
	console.log(meatCount+" meat - 1 free meat = "+"$"+meatTotal+".00");
	console.log("meat text1: "+text1);
	console.log("Purchase Total: "+"$"+runningTotal+".00");
	document.getElementById("showText").innerHTML=text1;
	document.getElementById("totalPrice").innerHTML = "<h3>Total: <strong>$"+runningTotal+".00"+"</strong></h3>";
	getVegetables(runningTotal,text1);
};
function getVegetables(runningTotal,text1) {
	var vegetablesTotal = 0;
	var selectedVegetables = [];
	var vegetablesArray = document.getElementsByClassName("vegetables");
	for (var k = 0; k < vegetablesArray.length; k++) {
		if (vegetablesArray[k].checked) {
			selectedVegetables.push(vegetablesArray[k].value);
			console.log("selected vegetables item: ("+vegetablesArray[k].value+")");
			text1 = text1+vegetablesArray[k].value+"<br>";
		}
	}
	var vegetablesCount = selectedVegetables.length;
	if (vegetablesCount > 1) {
		vegegablesTotal = (vegetablesCount - 1);
	} else {
		vegetablesTotal = 0;
	}
	runningTotal = (runningTotal + vegetablesTotal);
	console.log("total selected vegetables items: "+vegetablesCount);
	console.log(vegetablesCount+" vegetables - 1 free vegetables = "+"$"+vegetablesTotal+".00");
	console.log("vegetables text1: "+text1);
	console.log("Purchase Total: "+"$"+runningTotal+".00");
	document.getElementById("showText").innerHTML=text1;
	document.getElementById("totalPrice").innerHTML = "<h3>Total: <strong>$"+runningTotal+".00"+"</strong></h3>";
getCheese(runningTotal,text1);
};
function getCheese(runningTotal,text1) {
	var cheeseTotal = 0;
	var selectedCheese = [];
	var cheeseArray = document.getElementsByClassName("cheese");
	for (var l = 0; l < cheeseArray.length; l++) {
	if (cheeseArray[l].checked) {
			selectedCheese.push(cheeseArray[l].value);
			console.log("selected cheese item: ("+cheeseArray[l].value+")");
			text1 = text1+cheeseArray[l].value+"<br>";
		}
	}
	var cheeseCount = selectedCheese.length;
	if (cheeseCount > 1) {
		cheeseTotal = (cheeseCount - 1);
	} else {
		cheeseTotal = 0;
	}
	runningTotal = (runningTotal + cheeseTotal);
	console.log("total selected cheese items: "+cheeseCount);
	console.log(cheeseCount+" cheese - 1 free cheese = "+"$"+cheeseTotal+".00");
	console.log("cheese text1: "+text1);
	console.log("Purchase Total: "+"$"+runningTotal+".00");
	document.getElementById("showText").innerHTML=text1;
	document.getElementById("totalPrice").innerHTML = "<h3>Total: <strong>$"+runningTotal+".00"+"</strong></h3>";
getCrust(runningTotal,text1);
	};
function getCrust(runningTotal,text1) {
	var crustTotal = 0;
	var selectedCrust = [];
	var crustArray = document.getElementsByClassName("crust");
	for (var m = 0; m < crustArray.length; m++) {
		if (crustArray[m].checked) {
			selectedCrust.push(crustArray[m].value);
			console.log("selected crust item: ("+crustArray[m].value+")");
			text1 = text1+crustArray[m].value+"<br>";
		}
	}
	var crustCount = selectedCrust.length;
	if (crustCount > 1) {
		crustTotal = (crustCount - 1);
	} else {
		crustTotal = 0;
	}
	runningTotal = (runningTotal + crustTotal);
	console.log("total selected crustitems: "+crustCount);
	console.log(crustCount+" crust - 1 free crust = "+"$"+crustTotal+".00");
	console.log("crust text1: "+text1);
	console.log("Purchase Total: "+"$"+runningTotal+".00");
	document.getElementById("showText").innerHTML=text1;
	document.getElementById("totalPrice").innerHTML = "<h3>Total: <strong>$"+runningTotal+".00"+"</strong></h3>";
getSauce(runningTotal,text1);
	};
function getSauce(runningTotal,text1) {
	var sauceTotal = 0;
	var selectedSauce = [];
	var sauceArray = document.getElementsByClassName("sauce");
	for (var n = 0; n < sauceArray.length; n++) {
		if (sauceArray[n].checked) {
			selectedSauce.push(sauceArray[n].value);
			console.log("selected cheese item: ("+sauceArray[n].value+")");
			text1 = text1+sauceArray[n].value+"<br>";
		}
	}
	var sauceCount = selectedSauce.length;
	if (sauceCount > 1) {
		sauceTotal = (sauceCount - 1);
	} else {
		sauceTotal = 0;
	}
	runningTotal = (runningTotal + sauceTotal);
	console.log("total selected sauce items: "+sauceCount);
	console.log(sauceCount+" sauce - 1 free sauce = "+"$"+sauceTotal+".00");
	console.log("sauce text1: "+text1);
	console.log("Purchase Total: "+"$"+runningTotal+".00");
	document.getElementById("showText").innerHTML=text1;
	document.getElementById("totalPrice").innerHTML = "<h3>Total: <strong>$"+runningTotal+".00"+"</strong></h3>";
};
