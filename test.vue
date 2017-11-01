<template>
  <Table :columns="columns1" :data="data1"></Table>
</template>
<script>
export default {
  data() {
    return {
      columns1: [
        {
          title: "name",
          key: "name"
        },
        {
          title: "age",
          key: "age"
        },
        {
          title: "address",
          key: "address"
        }
      ],
      data1: [
        {
          name: "John Doe",
          age: 18,
          address: "Beijing"
        },
        {
          name: "Jane Doe",
          age: 25,
          address: "Shanghai"
        }
      ]
    };
  }
};
</script>