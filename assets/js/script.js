const toggleElement = (elementId, elementContentId) => {
  const element = document.getElementById(elementId);
  console.log(element);
  element.addEventListener("click", () => {
    const elementContent = document.getElementById(elementContentId);
    if (elementContent.classList.contains("hidden")) {
      elementContent.classList.remove("hidden");
    } else {
      elementContent.classList.add("hidden");
    }
  });
};

document.addEventListener("DOMContentLoaded", () => {
  toggleElement("work_mode", "work_mode_content");
  toggleElement("employement_type", "employement_type_content");
  toggleElement("experience", "experience_content");
  toggleElement("sector", "sector_content");
  toggleElement("regions", "regions_content");

  
});


const element = document.getElementById("menu_button");
element.addEventListener("click", () => {
  const elementContent = document.getElementById("menus");
  if (elementContent.classList.contains("hidden")) {
    elementContent.classList.remove("hidden");
  } else {
    elementContent.classList.add("hidden");
  }
});
