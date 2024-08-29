const isAdminCheckbox = document.getElementById("is_admin");
const classcodeContainer = document.getElementById("classcode-container");
const classcodeInput = document.getElementById("classcode");
const classcodeError = document.getElementById("classcode-error");

isAdminCheckbox.addEventListener("change", function () {
  if (this.checked) {
    classcodeContainer.style.display = "none";
    classcodeInput.removeAttribute("required");
  } else {
    classcodeContainer.style.display = "block";
    classcodeInput.setAttribute("required", "required");
  }
});

if (isAdminCheckbox.checked) {
  classcodeContainer.style.display = "none";
  classcodeInput.removeAttribute("required");
}

classcodeInput.addEventListener("blur", function () {
  const classcode = classcodeInput.value;
  if (classcode) {
    fetch(`/validate_classcode?classcode=${classcode}`)
      .then((response) => response.json())
      .then((data) => {
        if (!data.valid) {
          classcodeError.style.display = "block";
        } else {
          classcodeError.style.display = "none";
        }
      });
  }
});
