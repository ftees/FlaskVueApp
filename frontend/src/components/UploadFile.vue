<template>
  <div>
    <v-file-input label="File input" @change.native="upload"></v-file-input>
    <v-select label="Select" :items="csvHeader"></v-select>
  </div>
</template>

<script setup>
import { ref, onMounted, defineEmits } from "vue";
import Papa from 'papaparse';

const emits = defineEmits(["file-uploaded"]);

const selectedFile = ref(null);
const uploadStatus = ref("");
const csvHeader = ref([])

const upload = async (e) => {
  selectedFile.value = e.target.files[0]
  if (!selectedFile.value) {
    alert("Please select a file before uploading.");
    return;
  }
  readCsv(selectedFile.value)
  const formData = new FormData();
  formData.append("file", selectedFile.value);

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

const readCsv = (file) => {
  Papa.parse(file, {
    header: true,
    dynamicTyping: true,
    complete: (results) => {
      if (results.data.length > 0) {
        csvHeader.value = Object.keys(results.data[0]);
      }
    },
    error: (error) => {
      console.error('CSV Parsing Error:', error.message);
    },
  });
}



onMounted(() => {
  selectedFile.value = null;
  uploadStatus.value = "";
});
</script>

<style scoped>
/* Add your styling here if needed */
</style>