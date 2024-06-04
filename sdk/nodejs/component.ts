// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as splight from "@splightplatform/pulumi-splight";
 *
 * const componentTest = new splight.Component("componentTest", {
 *     description: "Created with Terraform",
 *     version: "Random-3.1.0",
 *     inputs: [
 *         {
 *             name: "period",
 *             type: "int",
 *             value: JSON.stringify(10),
 *             multiple: false,
 *             required: false,
 *             sensitive: false,
 *             description: "",
 *         },
 *         {
 *             name: "min",
 *             type: "int",
 *             value: JSON.stringify(1),
 *             multiple: false,
 *             required: false,
 *             sensitive: false,
 *             description: "",
 *         },
 *         {
 *             name: "max",
 *             type: "int",
 *             value: JSON.stringify(150),
 *             multiple: false,
 *             required: false,
 *             sensitive: false,
 *             description: "",
 *         },
 *         {
 *             name: "max_iterations",
 *             type: "int",
 *             value: JSON.stringify(3),
 *             multiple: false,
 *             required: false,
 *             sensitive: false,
 *             description: "",
 *         },
 *         {
 *             name: "should_crash",
 *             type: "bool",
 *             value: JSON.stringify("true"),
 *             multiple: false,
 *             required: false,
 *             sensitive: false,
 *             description: "",
 *         },
 *     ],
 * });
 * ```
 *
 * ## Import
 *
 * ```sh
 * $ pulumi import splight:index/component:Component [options] splight_component.<name> <component_id>
 * ```
 */
export class Component extends pulumi.CustomResource {
    /**
     * Get an existing Component resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ComponentState, opts?: pulumi.CustomResourceOptions): Component {
        return new Component(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'splight:index/component:Component';

    /**
     * Returns true if the given object is an instance of Component.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Component {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Component.__pulumiType;
    }

    /**
     * optinal description to add details of the resource
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The input parameters based on hubcomponent spec
     */
    public readonly inputs!: pulumi.Output<outputs.ComponentInput[]>;
    /**
     * the name of the component to be created
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * [NAME-VERSION] the version of the hub component
     */
    public readonly version!: pulumi.Output<string>;

    /**
     * Create a Component resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ComponentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ComponentArgs | ComponentState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ComponentState | undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["inputs"] = state ? state.inputs : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["version"] = state ? state.version : undefined;
        } else {
            const args = argsOrState as ComponentArgs | undefined;
            if ((!args || args.inputs === undefined) && !opts.urn) {
                throw new Error("Missing required property 'inputs'");
            }
            if ((!args || args.version === undefined) && !opts.urn) {
                throw new Error("Missing required property 'version'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["inputs"] = args ? args.inputs : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["version"] = args ? args.version : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Component.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Component resources.
 */
export interface ComponentState {
    /**
     * optinal description to add details of the resource
     */
    description?: pulumi.Input<string>;
    /**
     * The input parameters based on hubcomponent spec
     */
    inputs?: pulumi.Input<pulumi.Input<inputs.ComponentInput>[]>;
    /**
     * the name of the component to be created
     */
    name?: pulumi.Input<string>;
    /**
     * [NAME-VERSION] the version of the hub component
     */
    version?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Component resource.
 */
export interface ComponentArgs {
    /**
     * optinal description to add details of the resource
     */
    description?: pulumi.Input<string>;
    /**
     * The input parameters based on hubcomponent spec
     */
    inputs: pulumi.Input<pulumi.Input<inputs.ComponentInput>[]>;
    /**
     * the name of the component to be created
     */
    name?: pulumi.Input<string>;
    /**
     * [NAME-VERSION] the version of the hub component
     */
    version: pulumi.Input<string>;
}
