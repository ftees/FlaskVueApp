<template>
  <div>
    <v-file-input label="File input" @change="upload"></v-file-input>
    <v-select label="Select" :items="csvHeader"></v-select>
  </div>
</template>

<script>
import Papa from "papaparse";

export default {
  data() {
    return {
      selectedFile: null,
      uploadStatus: "",
      csvHeader: [],
    };
  },
  methods: {
    async upload(e) {
      this.selectedFile = e.target.files[0];
      if (!this.selectedFile) {
        alert("Please select a file before uploading.");
        return;
      }
      this.readCsv(this.selectedFile);
      const formData = new FormData();
      formData.append("file", this.selectedFile);

      try {
        const response = await fetch(
          `${process.env.VUE_APP_API_BASE_URL}/upload`,
          {
            method: "POST",
            body: formData,
          }
        );

        const responseData = await response.json();

        if (response.ok) {
          console.log("Server response:", responseData.message);
          this.uploadStatus = "File uploaded successfully!";
        } else {
          this.uploadStatus = `Error: ${responseData.error}`;
        }
      } catch (error) {
        console.error("Error during file upload:", error);
        this.uploadStatus = "Error during file upload. Please try again.";
      }
    },
    readCsv(file) {
      Papa.parse(file, {
        header: true,
        dynamicTyping: true,
        complete: (results) => {
          if (results.data.length > 0) {
            this.csvHeader = Object.keys(results.data[0]);
          }
        },
        error: (error) => {
          console.error("CSV Parsing Error:", error.message);
        },
      });
    },
  },
  mounted() {
    this.selectedFile = null;
    this.uploadStatus = "";
  },
};
</script>

<style scoped>
/* Add your styling here if needed */
</style>
