<template>
  <v-stepper v-model="currentStep" :items="['Step 1', 'Step 2', 'Step 3']"
    :next-text="currentStep === 2 ? 'Train' : 'Next'" @update:modelValue="handleClickNext">
    <template v-slot:item.1>
      <v-card title="Dataset" flat>
        <upload-file @update:selectColumn="handleSelectColumn" @update:uploadFile="handleUploadFile" />
      </v-card>
    </template>

    <template v-slot:item.2>
      <v-card title="Model" flat>
        <model-selector @update:optionModel="handleChangeOptionModel" @getFormModel="handleGetFormModel"></model-selector>
      </v-card>
    </template>

    <template v-slot:item.3>
      <v-card flat>
        <training-section :training="!token" :trainingComplete="token.length > 0" :token="token"></training-section>
      </v-card>
    </template>
  </v-stepper>
</template>

<script>
import UploadFile from "@/components/UploadFile.vue";
import ModelSelector from "@/components/ModelSelector.vue";
import TrainingSection from "@/components/TrainingSection.vue";

const PREFIX_URL = 'http://localhost:5000'

export default {
  components: {
    UploadFile,
    ModelSelector,
    TrainingSection,
  },
  data() {
    return {
      currentStep: 0,
      modelParams: undefined,
      selectedFile: '',
      selectedColumn: '',
      formModel: '',
      token: ''
    };
  },
  methods: {
    handleSelectColumn(e) {
      this.selectedColumn = e.toString()
    },
    handleUploadFile(e) {
      this.selectedFile = e
    },
    handleChangeOptionModel(e) {
      this.modelParams = e;
    },
    handleGetFormModel(e) {
      this.formModel = e
    },
    async handleClickNext() {
      if (this.currentStep === 2) {
        const formData = new FormData();
        formData.append("file", this.selectedFile);
        // formData.append("predict_column", this.selectedColumn);
        try {
          const response = await fetch(`${PREFIX_URL}/api/upload`, {
            method: "POST",
            body: formData,
          });

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
      }
      if (this.currentStep === 3) {
        await fetch(`${PREFIX_URL}/api/train`, {
          method: "POST",
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.formModel),
        }).then(response => response.json())
          .then(result => {
            this.token = result?.token
          })
      }
    },
  },
};
</script>
