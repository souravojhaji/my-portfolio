<template>
  <div class="about-me-container">
    <!-- Loop through each item in the about array -->
    <div v-for="(section, index) in about" :key="index" class="about-me-section">
      <h1 class="about-me-header">{{ section.title }}</h1>
      <!-- Render HTML content dynamically -->
      <p class="about-me-description" v-html="section.content"></p>
    </div>

    <!-- Loading message while data is being fetched -->
    <p v-if="about.length === 0" class="loading">Loading...</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      about: [] // Initialize as an empty array
    };
  },
  async mounted() {
    try {
      const response = await fetch('http://localhost:8000/api/about/');
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      this.about = data; // Load the entire response into the about array
    } catch (error) {
      console.error('Error fetching about data:', error);
    }
  }
};
</script>

<style scoped>
.about-me-container {
  display: flex;
  flex-direction: column;
  align-items: center; /* Center horizontally */
  justify-content: center; /* Center vertically */
  min-height: 100vh; /* Ensure it takes up full height of the viewport */
  padding: 40px 20px; /* Adjusted padding */
  background-color: #f0f8ff; /* Light background color */
}

.about-me-section {
  max-width: 800px; /* Constrain the content width */
  margin: 20px 0; /* Margin between sections */
  background-color: #fff;
  padding: 20px;
  border-radius: 12px; /* More rounded corners */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Slightly larger shadow */
}

.about-me-header {
  font-size: 2.5em; /* Adjusted font size */
  font-weight: bold;
  color: #333;
  margin-bottom: 10px;
  letter-spacing: 1.5px; /* Add spacing for a better look */
}

.about-me-description {
  font-size: 1.2em; /* Adjusted font size */
  color: #666;
  line-height: 1.6; /* Better line height for readability */
}

.loading {
  font-size: 1.5em; /* Adjusted font size */
  color: #888;
}
</style>
