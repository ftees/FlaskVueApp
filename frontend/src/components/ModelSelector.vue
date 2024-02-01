<template>
  <div>
    <v-select label="Model" :items="['XGBoost', 'Classifier', 'Regressor', 'K-means']"
      @update:modelValue="onModelChange"></v-select>
    <div class="slider-container">
      <span>Train part</span>
      <v-slider v-model="slider" class="align-center" hide-details :max="100" :min="0" :step="1">
        <template v-slot:append>
          <v-text-field v-model="slider" hide-details single-line density="compact" type="number"
            style="width: 70px"></v-text-field>
        </template>
      </v-slider>
    </div>
    <v-expansion-panels>
      <v-expansion-panel title="Modal options">
        <v-expansion-panel-text>
          <div class="option-model">
            <v-text-field v-for="(fieldName, index) in fieldList" :key="index" v-model="optionModel[fieldName]"
              :label="fieldName"></v-text-field>
          </div>
        </v-expansion-panel-text>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script>
import ModelParams from './data/ModelParams'

const modelTrainPart = {
  XGBoost: 20,
  Classifier: 45,
  Regressor: 55,
  "K-means": 66,
}

export default {
  data() {
    return {
      slider: 0,
      ModelParams,
      selectedModel: '',
      optionModel: {
        N_estimators: '',
        Max_depth: '',
        Learning_rate: null,
        Early_stopping_rounds: null,
      },
      fieldList: [
        'N_estimators',
        'Max_depth',
        'Learning_rate',
        'Early_stopping_rounds',
      ],
    };
  },

  methods: {
    async onModelChange(e) {
      this.fieldList = ModelParams[e]
      this.optionModel = Object.fromEntries(this.fieldList.map(fieldName => [fieldName, '']));
      this.slider = modelTrainPart[e]
      const data = {
        model: e,
        clusters: this.optionModel.clusters || 1
      }
      this.$emit('getFormModel', data)

    }
  },
  watch: {
    optionModel: {
      deep: true,
      handler(newVal) {
        this.$emit('update:optionModel', newVal);
      }
    }
  }
};
</script>

<style scoped>
.slider-container {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 20px;
}
</style>
