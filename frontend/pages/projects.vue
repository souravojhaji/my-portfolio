<template>
    <div class="projects-container">
      <h1 class="projects-header">Projects</h1>
      <ul class="projects-list">
        <li v-for="project in projects" :key="project.id" class="project-item">
          <a :href="project.url" class="project-title" target="_blank">{{ project.title }}</a>
          <p class="project-description">{{ project.description }}</p>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        projects: []
      };
    },
    async mounted() {
      const response = await fetch('http://localhost:8000/api/projects/');
      const data = await response.json();
      this.projects = data;
    }
  };
  </script>
  
  <style scoped>
.projects-container {
  text-align: center;
  padding: 40px; /* Increased padding for better spacing */
  background-color: #f0f8ff; /* Light background color */
  border-radius: 12px; /* Slightly larger border radius */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15); /* Enhanced shadow */
  max-width: 600px; /* Adjusted maximum width to match the contact container */
  margin: 40px auto; /* Added margin for spacing from other elements */
  color: #333; /* Dark text for better contrast */
}

  
  .projects-header {
    font-size: 32px;
    font-weight: bold;
    color: #333;
    margin-bottom: 20px;
  }
  
  .projects-list {
    list-style-type: none;
    padding: 0;
  }
  
  .project-item {
    margin-bottom: 20px;
  }
  
  .project-title {
    font-size: 24px;
    font-weight: bold;
    color: #007bff;
    text-decoration: none;
  }
  
  .project-title:hover {
    text-decoration: underline;
  }
  
  .project-description {
    font-size: 16px;
    color: #666;
    margin-top: 5px;
  }
  </style>
  