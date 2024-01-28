<template>
  <div>
    <v-select
      label="Model"
      :items="['XGBoost', 'Classifier', 'Regressor']"
    ></v-select>
    <div class="slider-contaner">
      <span>Train part</span>
      <v-slider
        v-model="slider"
        class="align-center"
        hide-details
        :max="100"
        :min="0"
        :step="1"
      >
        <template v-slot:append>
          <v-text-field
            v-model="slider"
            hide-details
            single-line
            density="compact"
            type="number"
            style="width: 70px"
          ></v-text-field>
        </template>
      </v-slider>
    </div>
    <v-expansion-panels>
      <v-expansion-panel title="Modal options">
        <v-expansion-panel-text>
          <div class="option-model">
            <v-text-field
              v-for="(fieldName, index) in fieldList"
              :key="index"
              v-model="optionModel[fieldName]"
              :label="fieldName"
            ></v-text-field>
          </div>
        </v-expansion-panel-text>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script setup>
import { ref } from "vue";

const slider = ref(0);
// Todo: Hard fix, will dynamic update when get from API
const optionModel = ref({
  N_estimators: "",
  Max_depth: "",
  Learning_rate: null,
  Early_stopping_rounds: null,
});

// Todo: Hard fix, will dynamic update when get from API
const fieldList = ref([
  "N_estimators",
  "Max_depth",
  "Learning_rate",
  "Early_stopping_rounds",
]);
</script>

<style scoped>
.slider-contaner {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 20px;
}
</style>
