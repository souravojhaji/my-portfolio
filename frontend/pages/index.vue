<template>
  <header class="intro-header">
    <div class="intro-inner-container">
      <p class="intro-text">Hi! I'm <strong>Sourav Ojha</strong>, a passionate software developer specializing in <strong>Python</strong> and <strong>Django</strong>.</p>
    </div>
  </header>
</template>

<style scoped>
.intro-header {
  padding: 40px; /* Padding for the header */
  background-color: #f5f5f5; /* Light background */
}

.intro-inner-container {
  max-width: 800px; /* Max width for the inner container */
  margin: 0 auto; /* Center the container */
  text-align: center; /* Center text */
  background-color: #fff; /* White background for inner container */
  border-radius: 12px; /* Rounded corners */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Light shadow for depth */
  padding: 30px; /* Padding inside the inner container */
}

.intro-text {
  font-size: 24px; /* Font size for intro text */
  color: #333; /* Dark text color */
  font-weight: 500; /* Medium font weight */
}

.intro-text strong {
  color: #007bff; /* Highlight important text in a different color */
}

@media (max-width: 768px) {
  .intro-text {
    font-size: 20px; /* Smaller font size for mobile */
    padding: 20px;
  }
}

@media (max-width: 480px) {
  .intro-text {
    font-size: 18px; /* Even smaller font size for very small screens */
    padding: 15px;
  }
}
</style>
