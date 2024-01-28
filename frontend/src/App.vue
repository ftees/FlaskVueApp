<!-- src/views/Home.vue -->
<template>
  <div class="main-container">
    <UploadTrainingPage />
  </div>
</template>

<script>
import UploadTrainingPage from "@/pages/UploadTrainingPage.vue";
import "./main.css";

export default {
  components: {
    UploadTrainingPage,
  },
  data() {
    return {
      selectedModelType: "classifier",
      selectedParameters: {},
      uploadStatus: null, // Added to track the file upload status
    };
  },
  methods: {
    updateModelType(value) {
      this.selectedModelType = value;
    },
    updateSelectedParameters(parameters) {
      this.selectedParameters = parameters;
    },
    handleFileUploaded(file) {
      // Handle the uploaded file as needed
      console.log("File uploaded:", file);

      // Send the file to the server and handle the response
      this.uploadFile(file);
    },
    async uploadFile(file) {
      const formData = new FormData();
      formData.append("file", file);

      try {
        const response = await fetch("api/upload", {
          method: "POST",
          body: formData,
        });

        const data = await response.json();

        if (response.ok) {
          // File uploaded successfully
          this.uploadStatus = "File uploaded successfully!";
        } else {
          // Handle error from the server
          this.uploadStatus = `Error: ${data.error}`;
        }
      } catch (error) {
        console.error("Error during file upload:", error);
        this.uploadStatus = "Error during file upload. Please try again.";
      }
    },
  },
};
</script>

<style scoped>
/* Add your styling here if needed */
</style>
