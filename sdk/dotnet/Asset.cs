// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Splight.Splight
{
    /// <summary>
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using System.Text.Json;
    /// using Pulumi;
    /// using Splight = Splight.Splight;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var assetMainTest = new Splight.Asset("assetMainTest", new()
    ///     {
    ///         Description = "Created with Terraform",
    ///         Geometry = JsonSerializer.Serialize(new Dictionary&lt;string, object?&gt;
    ///         {
    ///             ["type"] = "GeometryCollection",
    ///             ["geometries"] = new[]
    ///             {
    ///             },
    ///         }),
    ///         Kinds = new[]
    ///         {
    ///             new Splight.Inputs.AssetKindArgs
    ///             {
    ///                 Id = "1234-1234-1234-1234",
    ///                 Name = "Line",
    ///             },
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// ```sh
    /// $ pulumi import splight:index/asset:Asset [options] splight_asset.&lt;name&gt; &lt;asset_id&gt;
    /// ```
    /// </summary>
    [SplightResourceType("splight:index/asset:Asset")]
    public partial class Asset : global::Pulumi.CustomResource
    {
        /// <summary>
        /// description of the resource
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// geo position and shape of the resource
        /// </summary>
        [Output("geometry")]
        public Output<string?> Geometry { get; private set; } = null!;

        /// <summary>
        /// kind of the resource
        /// </summary>
        [Output("kinds")]
        public Output<ImmutableArray<Outputs.AssetKind>> Kinds { get; private set; } = null!;

        /// <summary>
        /// name of the resource
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// linked assets
        /// </summary>
        [Output("relatedAssets")]
        public Output<ImmutableArray<string>> RelatedAssets { get; private set; } = null!;


        /// <summary>
        /// Create a Asset resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Asset(string name, AssetArgs? args = null, CustomResourceOptions? options = null)
            : base("splight:index/asset:Asset", name, args ?? new AssetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Asset(string name, Input<string> id, AssetState? state = null, CustomResourceOptions? options = null)
            : base("splight:index/asset:Asset", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/splightplatform",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Asset resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Asset Get(string name, Input<string> id, AssetState? state = null, CustomResourceOptions? options = null)
        {
            return new Asset(name, id, state, options);
        }
    }

    public sealed class AssetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// description of the resource
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// geo position and shape of the resource
        /// </summary>
        [Input("geometry")]
        public Input<string>? Geometry { get; set; }

        [Input("kinds")]
        private InputList<Inputs.AssetKindArgs>? _kinds;

        /// <summary>
        /// kind of the resource
        /// </summary>
        public InputList<Inputs.AssetKindArgs> Kinds
        {
            get => _kinds ?? (_kinds = new InputList<Inputs.AssetKindArgs>());
            set => _kinds = value;
        }

        /// <summary>
        /// name of the resource
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("relatedAssets")]
        private InputList<string>? _relatedAssets;

        /// <summary>
        /// linked assets
        /// </summary>
        public InputList<string> RelatedAssets
        {
            get => _relatedAssets ?? (_relatedAssets = new InputList<string>());
            set => _relatedAssets = value;
        }

        public AssetArgs()
        {
        }
        public static new AssetArgs Empty => new AssetArgs();
    }

    public sealed class AssetState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// description of the resource
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// geo position and shape of the resource
        /// </summary>
        [Input("geometry")]
        public Input<string>? Geometry { get; set; }

        [Input("kinds")]
        private InputList<Inputs.AssetKindGetArgs>? _kinds;

        /// <summary>
        /// kind of the resource
        /// </summary>
        public InputList<Inputs.AssetKindGetArgs> Kinds
        {
            get => _kinds ?? (_kinds = new InputList<Inputs.AssetKindGetArgs>());
            set => _kinds = value;
        }

        /// <summary>
        /// name of the resource
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("relatedAssets")]
        private InputList<string>? _relatedAssets;

        /// <summary>
        /// linked assets
        /// </summary>
        public InputList<string> RelatedAssets
        {
            get => _relatedAssets ?? (_relatedAssets = new InputList<string>());
            set => _relatedAssets = value;
        }

        public AssetState()
        {
        }
        public static new AssetState Empty => new AssetState();
    }
}
