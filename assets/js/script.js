

const toggleElement = (elementId, elementContentId) => {
  const workMode = document.getElementById(elementId);
  workMode.addEventListener("click", () => {
    const workModeContent = document.getElementById(elementContentId);
    if (workModeContent.classList.contains("hidden")) {
      workModeContent.classList.remove("hidden");
    } else {
      workModeContent.classList.add("hidden");
    }
  });
};

toggleElement("work_mode", "work_mode_content")
toggleElement("employement_type", "employement_type_content")
toggleElement("experience", "experience_content")
toggleElement("sector", "sector_content")