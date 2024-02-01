<template>
  <div>
    <v-file-input label="File input" @change="upload"></v-file-input>
    <v-select label="Select" :items="csvHeader" @update:modelValue="onSelectColumn"></v-select>
  </div>
</template>

<script>
import Papa from "papaparse";

export default {
  data() {
    return {
      selectedFile: null,
      selectedColumn: '',
      uploadStatus: "",
      csvHeader: [],
    };
  },
  methods: {
    onSelectColumn(e) {
      this.selectedColumn = e
      this.$emit('update:selectColumn', this.selectedColumn);
    },
    async upload(e) {
      this.selectedFile = e.target.files[0];
      if (!this.selectedFile) {
        alert("Please select a file before uploading.");
        return;
      }
      this.readCsv(this.selectedFile);
      this.$emit('update:uploadFile', this.selectedFile);
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
