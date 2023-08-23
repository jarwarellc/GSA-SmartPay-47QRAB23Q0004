<!-- ProgrammaticDataDashboard.vue -->
<template>
  <div>
    <!-- JarWare Developer: Display dashboard interface and fetch data button -->
    <h1>Programmatic Data Dashboard</h1>
    <p>Explore agency spend data and trends.</p>
    <button @click="fetchData">Fetch Data</button>
    <div v-if="dataFetched">
      <!-- JarWare Developer: Display fetched data visualization components -->
      <div v-for="(data, index) in fetchedData" :key="index">
        {{ data.name }}: {{ data.value }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dataFetched: false,
      fetchedData: [],
    };
  },
  methods: {
    fetchData() {
      // JarWare Developer: Simulate fetching data from an API
      setTimeout(() => {
        this.dataFetched = true;
        this.fetchedData = [
          { name: 'Agency A', value: 1000000 },
          { name: 'Agency B', value: 750000 },
          // ...other fetched data
        ];
      }, 1000);
    },
  },
};
</script>
