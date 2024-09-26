<template>
    <div class="contact-info-container">
      <h2 class="contact-info-header">Contact Information</h2>
      <div class="contact-details">
        <p><strong>Email:</strong> <a :href="'mailto:' + contact.email" class="contact-link">{{ contact.email }}</a></p>
        <p><strong>Phone:</strong> <a :href="'tel:' + contact.phone" class="contact-link">{{ contact.phone }}</a></p>
        <p><strong>GitHub:</strong> <a :href="contact.github" target="_blank" class="contact-link">{{ contact.github }}</a></p>
      </div>
    </div>
  </template>

<script>
export default {
  data() {
    return {
      contact: {}
    };
  },
  async mounted() {
    const contactResponse = await fetch('http://localhost:8000/api/contact-info/');
    const contactData = await contactResponse.json();
    if (contactData.length > 0) {
      this.contact = contactData[0]; // Assuming the API returns an array
    }
  }
};
</script>
  
  <style scoped>
  .contact-info-container {
    text-align: center;
    padding: 40px; /* Increased padding for better spacing */
    background-color: #f0f8ff; /* Light background color */
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    max-width: 600px;
    margin: 40px auto; /* Added margin for spacing from other elements */
    color: #333; /* Dark text for better contrast */
  }
  
  .contact-info-header {
    font-size: 32px; /* Increased font size for header */
    font-weight: bold;
    margin-bottom: 20px;
    color: #333; /* Darker color for header */
  }
  
  .contact-details p {
    font-size: 20px; /* Adjusted font size */
    color: #555; /* Slightly lighter text color */
    margin-bottom: 15px; /* Increased spacing between paragraphs */
  }
  
  .contact-link {
    color: #007bff; /* Blue for links */
    text-decoration: none;
    font-weight: bold;
    transition: color 0.3s; /* Smooth transition for hover effect */
  }
  
  .contact-link:hover {
    color: #0056b3; /* Darker blue on hover */
    text-decoration: underline;
  }
  </style>
  