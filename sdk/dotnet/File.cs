// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Splight
{
    /// <summary>
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Splight = Pulumi.Splight;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var fileInnerTest = new Splight.File("fileInnerTest", new()
    ///     {
    ///         Description = "Sample file for testing inner file",
    ///         Parent = "1234-1234-1234-1234",
    ///         Path = "./variables.tf",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// ```sh
    /// $ pulumi import splight:index/file:File [options] splight_file.&lt;name&gt; &lt;file_id&gt;
    /// ```
    /// </summary>
    [SplightResourceType("splight:index/file:File")]
    public partial class File : global::Pulumi.CustomResource
    {
        [Output("checksum")]
        public Output<string> Checksum { get; private set; } = null!;

        /// <summary>
        /// complementary information to describe the file
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// the id reference for a folder to be placed in
        /// </summary>
        [Output("parent")]
        public Output<string?> Parent { get; private set; } = null!;

        /// <summary>
        /// the path for the file resource in your system
        /// </summary>
        [Output("path")]
        public Output<string> Path { get; private set; } = null!;

        /// <summary>
        /// assets to be linked
        /// </summary>
        [Output("relatedAssets")]
        public Output<ImmutableArray<string>> RelatedAssets { get; private set; } = null!;


        /// <summary>
        /// Create a File resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public File(string name, FileArgs args, CustomResourceOptions? options = null)
            : base("splight:index/file:File", name, args ?? new FileArgs(), MakeResourceOptions(options, ""))
        {
        }

        private File(string name, Input<string> id, FileState? state = null, CustomResourceOptions? options = null)
            : base("splight:index/file:File", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing File resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static File Get(string name, Input<string> id, FileState? state = null, CustomResourceOptions? options = null)
        {
            return new File(name, id, state, options);
        }
    }

    public sealed class FileArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// complementary information to describe the file
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// the id reference for a folder to be placed in
        /// </summary>
        [Input("parent")]
        public Input<string>? Parent { get; set; }

        /// <summary>
        /// the path for the file resource in your system
        /// </summary>
        [Input("path", required: true)]
        public Input<string> Path { get; set; } = null!;

        [Input("relatedAssets")]
        private InputList<string>? _relatedAssets;

        /// <summary>
        /// assets to be linked
        /// </summary>
        public InputList<string> RelatedAssets
        {
            get => _relatedAssets ?? (_relatedAssets = new InputList<string>());
            set => _relatedAssets = value;
        }

        public FileArgs()
        {
        }
        public static new FileArgs Empty => new FileArgs();
    }

    public sealed class FileState : global::Pulumi.ResourceArgs
    {
        [Input("checksum")]
        public Input<string>? Checksum { get; set; }

        /// <summary>
        /// complementary information to describe the file
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// the id reference for a folder to be placed in
        /// </summary>
        [Input("parent")]
        public Input<string>? Parent { get; set; }

        /// <summary>
        /// the path for the file resource in your system
        /// </summary>
        [Input("path")]
        public Input<string>? Path { get; set; }

        [Input("relatedAssets")]
        private InputList<string>? _relatedAssets;

        /// <summary>
        /// assets to be linked
        /// </summary>
        public InputList<string> RelatedAssets
        {
            get => _relatedAssets ?? (_relatedAssets = new InputList<string>());
            set => _relatedAssets = value;
        }

        public FileState()
        {
        }
        public static new FileState Empty => new FileState();
    }
}