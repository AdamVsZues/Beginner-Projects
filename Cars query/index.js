var carInfoTypeOne = ["Make:", "Model:", "Year:", "Desription:"];
var carInfoOne = ["Hyundai", "Tuscon", "2022", "Red 2022 Hyundai Tuscon SEL"];

var bodyString = "";
$.each(carInfoTypeOne, function (index, ctry) {
  bodyString +=
    "<tr><td>" + ctry + "</td><td>" + carInfoOne[index] + "</td></tr>";
});
$(".carOneTable tbody").html(bodyString);

var carInfoTypeTwo = ["Make:", "Model:", "Year:", "Desription:"];
var carInfoTwo = ["Ford", "F150", "2016", "Black Ford F150 XLT"];

var bodyString = "";
$.each(carInfoTypeTwo, function (index, ctry) {
  bodyString +=
    "<tr><td>" + ctry + "</td><td>" + carInfoTwo[index] + "</td></tr>";
});
$(".carTwoTable tbody").html(bodyString);

// Sets the inputs to hyundai info for updating
document
  .getElementById("hyundaiButton")
  .addEventListener("click", function setCarOneInfo() {
    document.getElementById("carMake").value = carInfoOne[0];
    document.getElementById("carModel").value = carInfoOne[1];
    document.getElementById("carYear").value = carInfoOne[2];
    document.getElementById("carDescription").value = carInfoOne[3];
  });
// Sets the inputs to ford info for updating
document
  .getElementById("fordButton")
  .addEventListener("click", function setCarOneInfo() {
    document.getElementById("carMake").value = carInfoTwo[0];
    document.getElementById("carModel").value = carInfoTwo[1];
    document.getElementById("carYear").value = carInfoTwo[2];
    document.getElementById("carDescription").value = carInfoTwo[3];
  });

document
  .getElementById("update")
  .addEventListener("click", function updateCar() {
    document.getElementById("hyundaiButton");
    document.getElementById("fordButton");
    if (hyundaiButton.checked) {
      carInfoOne[0] = document.getElementById("carMake").value;
      carInfoOne[1] = document.getElementById("carModel").value;
      carInfoOne[2] = document.getElementById("carYear").value;
      carInfoOne[3] = document.getElementById("carDescription").value;
      var bodyString = "";
      $.each(carInfoTypeOne, function (index, ctry) {
        bodyString +=
          "<tr><td>" + ctry + "</td><td>" + carInfoOne[index] + "</td></tr>";
      });
      $(".carOneTable tbody").html(bodyString);
    } else if (fordButton.checked) {
      carInfoTwo[0] = document.getElementById("carMake").value;
      carInfoTwo[1] = document.getElementById("carModel").value;
      carInfoTwo[2] = document.getElementById("carYear").value;
      carInfoTwo[3] = document.getElementById("carDescription").value;

      var bodyString = "";
      $.each(carInfoTypeTwo, function (index, ctry) {
        bodyString +=
          "<tr><td>" + ctry + "</td><td>" + carInfoTwo[index] + "</td></tr>";
      });
      $(".carTwoTable tbody").html(bodyString);
    }
  });
