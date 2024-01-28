<template>
  <div>
    <v-file-input label="File input" @change.native="upload"></v-file-input>
    <v-select label="Select" :items="[
      'California',
      'Colorado',
      'Florida',
      'Georgia',
      'Texas',
      'Wyoming',
    ]"></v-select>
  </div>
</template>

<script setup>
import { ref, onMounted, defineEmits } from "vue";

const emits = defineEmits(["file-uploaded"]);

const selectedFile = ref(null);
const uploadStatus = ref("");

// const handleFileUpload = (event) => {
//   const file = event.target.files[0];

//   if (file && file.type === "text/csv") {
//     selectedFile.value = file;
//   } else {
//     // Reset selectedFile if the file is not a CSV
//     selectedFile.value = null;
//     alert("Please upload a valid CSV file.");
//   }
// };

const upload = async (e) => {
  console.log(e);
  selectedFile.value = e.target.files[0]
  if (!selectedFile.value) {
    alert("Please select a file before uploading.");
    return;
  }

  const formData = new FormData();
  formData.append("file", selectedFile.value);
  console.log(formData);
  try {
    const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/upload`, {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    if (response.ok) {
      console.log("Server response:", data.message);
      uploadStatus.value = "File uploaded successfully!";
    } else {
      uploadStatus.value = `Error: ${data.error}`;
    }
  } catch (error) {
    console.error("Error during file upload:", error);
    uploadStatus.value = "Error during file upload. Please try again.";
  }
};

// Clear selectedFile when the component is mounted
onMounted(() => {
  selectedFile.value = null;
  uploadStatus.value = "";
});
</script>

<style scoped>
/* Add your styling here if needed */
</style>
