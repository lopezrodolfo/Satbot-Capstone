const addNewEntryButton = document.getElementById("add-new-entry");
const closeButton = document.getElementById("close-button");
const previewContainer = document.getElementById("preview-container");
const overlay = document.getElementById("overlay");

addNewEntryButton.addEventListener("click", () => {
  previewContainer.style.display = "block";
  overlay.style.display = "block";
});

closeButton.addEventListener("click", () => {
  previewContainer.style.display = "none";
  overlay.style.display = "none";
});

const addNewPublicEntryButton = document.getElementById("add-new-public-entry");

addNewPublicEntryButton.addEventListener("click", () => {
  previewContainer.style.display = "block";
  overlay.style.display = "block";
});

const editButtons = document.querySelectorAll(".edit");
const editContainer = document.getElementById("edit-container");
const editCloseButton = document.getElementById("edit-close-button");

editButtons.forEach((editButton) => {
  editButton.addEventListener("click", () => {
    editContainer.style.display = "block";
    overlay.style.display = "block";
  });
});

editCloseButton.addEventListener("click", () => {
  editContainer.style.display = "none";
  overlay.style.display = "none";
});
