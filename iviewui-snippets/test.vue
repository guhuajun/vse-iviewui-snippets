<style>
.ivu-table .demo-table-info-row td {
  background-color: #2db7f5;
  color: #fff;
}
.ivu-table .demo-table-error-row td {
  background-color: #ff6600;
  color: #fff;
}
.ivu-table td.demo-table-info-column {
  background-color: #2db7f5;
  color: #fff;
}
.ivu-table .demo-table-info-cell-name {
  background-color: #2db7f5;
  color: #fff;
}
.ivu-table .demo-table-info-cell-age {
  background-color: #ff6600;
  color: #fff;
}
.ivu-table .demo-table-info-cell-address {
  background-color: #187;
  color: #fff;
}
</style>
<template>
  <Table :row-class-name="rowClassName" :columns="columns1" :data="data1"></Table>
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
      columns9: [
        {
          title: "name",
          key: "name"
        },
        {
          title: "age",
          key: "age",
          className: "demo-table-info-column"
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
          address: "Beijing"
        },
        {
          name: "Anna Smith",
          age: 30,
          address: "Shanghai"
        },
        {
          name: "Bob Smith",
          age: 26,
          address: "Shenzhen"
        }
      ],
      data8: [
        {
          name: "John Doe",
          age: 18,
          address: "Beijing"
        },
        {
          name: "Jane Doe",
          age: 25,
          address: "Beijing",
          cellClassName: {
            age: "demo-table-info-cell-age",
            address: "demo-table-info-cell-address"
          }
        },
        {
          name: "Anna Smith",
          age: 30,
          address: "Shanghai"
        },
        {
          name: "Bob Smith",
          age: 26,
          address: "Shenzhen",
          cellClassName: {
            name: "demo-table-info-cell-name"
          }
        }
      ]
    };
  },
  methods: {
    rowClassName(row, index) {
      if (index === 1) {
        return "demo-table-info-row";
      } else if (index === 3) {
        return "demo-table-error-row";
      }
      return "";
    }
  }
};
</script>