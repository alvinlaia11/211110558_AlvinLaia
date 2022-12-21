<template>
    <div>
    <div class="field">
        <label class="label">Product Name</label>
        <div class="control">
            <input
                class="input"
                type="text"
                placeholder="Product Name"
                v-model="productName"
            />
        </div>
    </div>
    <div class="field">
        <label class="label">Product Price</label>
        <div class="control">
            <input
                class="input"
                type="text"
                placeholder="Product Price"
                v-model="productPrice"
            />
        </div>
    </div>
    <div class="control">
        <button class="button is-success" @click="saveProduct">SAVE</button>
    </div>
</div>
</template>
<script>
// import axios
import axios from "axios";


export default {
    name: "ProductAdd",
    data() {
        return {
            productName: "",
            productPrice: "",
        };
    },
    methods: {
        // Create New product
        async saveProduct() {
            try {
                await axios.post("http://localhost:3000/api/products", {
                    product_name: this.productName,
                    product_price: this.productPrice,
                });
                this.productName = "";
                this.productPrice = "";
                this.$router.push("/");
            } catch (err) {
                console.log(err);
            }
        },
    },
};
</script>

<style>
</style