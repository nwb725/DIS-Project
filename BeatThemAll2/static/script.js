document.addEventListener("DOMContentLoaded", function () {
    console.log("Document loaded and script running.");

    const pokemonItems = document.querySelectorAll(".pokemon-item");

    pokemonItems.forEach(item => {
        item.addEventListener("mouseenter", function () {
            const speed = this.getAttribute("data-speed");
            const attack = this.getAttribute("data-attack");
            const defense = this.getAttribute("data-defense");

            console.log(`Hovering over ${this.querySelector(".pokemon-name").innerText}`);
            console.log(`Speed: ${speed}, Attack: ${attack}, Defense: ${defense}`);

            let tooltip = this.querySelector(".tooltip");
            if (tooltip) {
                console.log("Tooltip found, displaying...");
                tooltip.style.display = 'block';
            } else {
                console.log("Tooltip not found!");
            }
        });

        item.addEventListener("mouseleave", function () {
            console.log(`Mouse left ${this.querySelector(".pokemon-name").innerText}`);
            let tooltip = this.querySelector(".tooltip");
            if (tooltip) {
                tooltip.style.display = 'none';
            }
        });
    });
});
