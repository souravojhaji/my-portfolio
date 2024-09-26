<template>
  <div class="skills-container">
    <h1 class="skills-header">Skills</h1>
    <ul class="skills-list">
      <li v-for="skill in skills" :key="skill.id" class="skill-item">
        <span class="skill-name">{{ skill.name }}</span> - 
        <span class="skill-description">{{ skill.description }}</span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      skills: [] // Initialize the skills array
    };
  },
  async mounted() {
    try {
      const response = await fetch('http://localhost:8000/api/skills/');
      const data = await response.json();
      this.skills = data; // Set the fetched data to the skills array
    } catch (error) {
      console.error('Error fetching skills:', error);
    }
  }
};
</script>

<style scoped>
.skills-container {
  display: flex;
  flex-direction: column;
  align-items: center; /* Center the content horizontally */
  padding: 40px; /* Increased padding for better spacing */
  background-color: #f9f9f9; /* Light background color */
  min-height: 100vh; /* Make sure the section takes up the full height */
  text-align: center;
}

.skills-header {
  font-size: 36px; /* Font size for header */
  font-weight: bold;
  margin-bottom: 30px; /* Increased spacing below header */
  color: #333; /* Dark color for header */
}

.skills-list {
  list-style-type: none; /* Remove default bullet points */
  padding: 0;
}

.skill-item {
  font-size: 20px; /* Adjusted font size */
  color: #555; /* Slightly darker text color */
  margin-bottom: 15px; /* Spacing between skills */
  background-color: #fff; /* White background for skill items */
  padding: 15px; /* Padding inside each skill item */
  border-radius: 8px; /* Rounded corners */
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1); /* Light shadow for depth */
  width: 100%; /* Full width */
  max-width: 600px; /* Limit width */
  text-align: left; /* Align text to the left within the list */
  transition: transform 0.2s; /* Smooth scaling effect */
}

.skill-item:hover {
  transform: scale(1.02); /* Slightly enlarge on hover */
}

.skill-name {
  font-weight: bold; /* Bold text for skill names */
  color: #333; /* Darker color for skill names */
}

.skill-description {
  color: #777; /* Lighter color for descriptions */
}

@media (min-width: 768px) {
  .skill-item {
    font-size: 22px; /* Increase font size for larger screens */
  }
}
</style>
