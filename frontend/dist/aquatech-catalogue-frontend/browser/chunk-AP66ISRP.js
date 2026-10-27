import {
  Component,
  RouterLink,
  setClassMetadata,
  ɵsetClassDebugInfo,
  ɵɵdefineComponent,
  ɵɵelementEnd,
  ɵɵelementStart,
  ɵɵtext
} from "./chunk-WHRWH5J6.js";

// src/app/pages/contact.component.ts
var _ContactComponent = class _ContactComponent {
};
_ContactComponent.\u0275fac = function ContactComponent_Factory(__ngFactoryType__) {
  return new (__ngFactoryType__ || _ContactComponent)();
};
_ContactComponent.\u0275cmp = /* @__PURE__ */ \u0275\u0275defineComponent({ type: _ContactComponent, selectors: [["app-contact"]], decls: 35, vars: 0, consts: [[1, "page-banner"], [1, "container"], [1, "section"], [1, "row", "g-4"], [1, "col-12", "col-md-4"], [1, "contact-card"], ["routerLink", "/catalogue"], ["routerLink", "/about"], ["href", "https://wa.me/91XXXXXXXXXX?text=Hello%20Aakash%20AquaTech", "target", "_blank", "rel", "noopener noreferrer"]], template: function ContactComponent_Template(rf, ctx) {
  if (rf & 1) {
    \u0275\u0275elementStart(0, "section", 0)(1, "div", 1)(2, "small");
    \u0275\u0275text(3, "GET IN TOUCH");
    \u0275\u0275elementEnd();
    \u0275\u0275elementStart(4, "h1");
    \u0275\u0275text(5, "Contact Aakash AquaTech");
    \u0275\u0275elementEnd();
    \u0275\u0275elementStart(6, "p");
    \u0275\u0275text(7, "We are here to help with product enquiries and service assistance.");
    \u0275\u0275elementEnd()()();
    \u0275\u0275elementStart(8, "section", 2)(9, "div", 1)(10, "div", 3)(11, "div", 4)(12, "div", 5)(13, "h3");
    \u0275\u0275text(14, "Our Products");
    \u0275\u0275elementEnd();
    \u0275\u0275elementStart(15, "p");
    \u0275\u0275text(16, "Explore our water purification products.");
    \u0275\u0275elementEnd();
    \u0275\u0275elementStart(17, "a", 6);
    \u0275\u0275text(18, "Browse Catalogue \u2192");
    \u0275\u0275elementEnd()()();
    \u0275\u0275elementStart(19, "div", 4)(20, "div", 5)(21, "h3");
    \u0275\u0275text(22, "Product Support");
    \u0275\u0275elementEnd();
    \u0275\u0275elementStart(23, "p");
    \u0275\u0275text(24, "Contact our team for product details and availability.");
    \u0275\u0275elementEnd();
    \u0275\u0275elementStart(25, "a", 7);
    \u0275\u0275text(26, "About Us \u2192");
    \u0275\u0275elementEnd()()();
    \u0275\u0275elementStart(27, "div", 4)(28, "div", 5)(29, "h3");
    \u0275\u0275text(30, "WhatsApp Enquiry");
    \u0275\u0275elementEnd();
    \u0275\u0275elementStart(31, "p");
    \u0275\u0275text(32, "Ask us about products and services.");
    \u0275\u0275elementEnd();
    \u0275\u0275elementStart(33, "a", 8);
    \u0275\u0275text(34, "Chat on WhatsApp \u2192");
    \u0275\u0275elementEnd()()()()()();
  }
}, dependencies: [RouterLink], encapsulation: 2 });
var ContactComponent = _ContactComponent;
(() => {
  (typeof ngDevMode === "undefined" || ngDevMode) && setClassMetadata(ContactComponent, [{
    type: Component,
    args: [{
      selector: "app-contact",
      standalone: true,
      imports: [RouterLink],
      template: `
    <section class="page-banner">
      <div class="container">
        <small>GET IN TOUCH</small>
        <h1>Contact Aakash AquaTech</h1>
        <p>We are here to help with product enquiries and service assistance.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="row g-4">
          <div class="col-12 col-md-4">
            <div class="contact-card">
              <h3>Our Products</h3>
              <p>Explore our water purification products.</p>
              <a routerLink="/catalogue">Browse Catalogue \u2192</a>
            </div>
          </div>

          <div class="col-12 col-md-4">
            <div class="contact-card">
              <h3>Product Support</h3>
              <p>Contact our team for product details and availability.</p>
              <a routerLink="/about">About Us \u2192</a>
            </div>
          </div>

          <div class="col-12 col-md-4">
            <div class="contact-card">
              <h3>WhatsApp Enquiry</h3>
              <p>Ask us about products and services.</p>
              <a
                href="https://wa.me/91XXXXXXXXXX?text=Hello%20Aakash%20AquaTech"
                target="_blank"
                rel="noopener noreferrer"
              >Chat on WhatsApp \u2192</a>
            </div>
          </div>
        </div>
      </div>
    </section>
  `
    }]
  }], null, null);
})();
(() => {
  (typeof ngDevMode === "undefined" || ngDevMode) && \u0275setClassDebugInfo(ContactComponent, { className: "ContactComponent", filePath: "src/app/pages/contact.component.ts", lineNumber: 52 });
})();
export {
  ContactComponent
};
//# sourceMappingURL=chunk-AP66ISRP.js.map
